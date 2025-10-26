import React, { useState, useEffect } from 'react'
import SpendingPieChart from './SpendingPieChart'

const API = 'http://localhost:5000'

const cardStyle = {
    maxWidth: 800,
    margin: '40px auto',
    background: '#fff',
    borderRadius: 12,
    boxShadow: '0 2px 16px #0002',
    padding: 32,
    fontFamily: 'Segoe UI, Arial, sans-serif',
}
const inputStyle = {
    width: '100%',
    padding: '10px',
    margin: '8px 0',
    borderRadius: 6,
    border: '1px solid #ccc',
    fontSize: 16,
}
const buttonStyle = {
    padding: '10px 18px',
    borderRadius: 6,
    border: 'none',
    background: '#d32f2f',
    color: '#fff',
    fontWeight: 600,
    fontSize: 16,
    cursor: 'pointer',
    marginRight: 8,
}
const switchStyle = {
    ...buttonStyle,
    background: '#d32f2f',
    color: '#fff',
    border: 'none',
}

export default function App() {
    const [mode, setMode] = useState('login') // 'login' or 'register' or 'hello'
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [token, setToken] = useState(localStorage.getItem('token') || '')
    const [message, setMessage] = useState('')
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState('')
    const [success, setSuccess] = useState('')
    // Plaid integration removed — clearing related UI state

    useEffect(() => {
        if (token) {
            setLoading(true)
            fetch(`${API}/api/hello`, { headers: { Authorization: `Bearer ${token}` } })
                .then(r => r.json())
                .then(data => {
                    setLoading(false)
                    if (data.message) {
                        setMessage(data.message)
                        setMode('hello')
                    } else {
                        setToken('')
                        localStorage.removeItem('token')
                    }
                })
                .catch(() => {
                    setLoading(false)
                    setToken('')
                    localStorage.removeItem('token')
                })
        }
    }, [token])

    function doRegister(e) {
        e.preventDefault()
        setLoading(true)
        setError('')
        setSuccess('')
        fetch(`${API}/api/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        })
            .then(r => r.json().then(body => ({ ok: r.ok, body })))
            .then(({ ok, body }) => {
                setLoading(false)
                if (ok) {
                    setSuccess('Registered! Please login.')
                    setMode('login')
                } else {
                    setError(body.error || 'Register failed')
                }
            })
    }

    function doLogin(e) {
        e.preventDefault()
        setLoading(true)
        setError('')
        setSuccess('')
        fetch(`${API}/api/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        })
            .then(r => r.json().then(body => ({ ok: r.ok, body })))
            .then(({ ok, body }) => {
                setLoading(false)
                if (ok && body.token) {
                    setToken(body.token)
                    localStorage.setItem('token', body.token)
                } else {
                    setError(body.error || 'Login failed')
                }
            })
    }

    function logout() {
        setToken('')
        localStorage.removeItem('token')
        setMode('login')
        setUsername('')
        setPassword('')
        setMessage('')
        setError('')
        setSuccess('')
    }

    // Transaction pagination state
    const [transactions, setTransactions] = useState([])
    const [page, setPage] = useState(1)
    const [totalTx, setTotalTx] = useState(0)
    const [hasNext, setHasNext] = useState(false)
    const [hasPrev, setHasPrev] = useState(false)
    const [txLoading, setTxLoading] = useState(false)

    // AI Chat state
    const [aiQuestion, setAiQuestion] = useState('')
    const [aiResponse, setAiResponse] = useState('')
    const [aiLoading, setAiLoading] = useState(false)
    const [showChat, setShowChat] = useState(false)

    // Cash flow state
    const [cashFlow, setCashFlow] = useState(null)
    const [cashFlowLoading, setCashFlowLoading] = useState(false)

    useEffect(() => {
        if (mode === 'hello' && token) {
            setTxLoading(true)
            fetch(`${API}/api/transactions?page=${page}&per_page=10`, {
                headers: { Authorization: `Bearer ${token}` }
            })
                .then(r => r.json())
                .then(data => {
                    setTransactions(data.transactions || [])
                    setTotalTx(data.total || 0)
                    setHasNext(data.has_next || false)
                    setHasPrev(data.has_prev || false)
                    setTxLoading(false)
                })
                .catch(() => {
                    setTransactions([])
                    setTotalTx(0)
                    setHasNext(false)
                    setHasPrev(false)
                    setTxLoading(false)
                })
        }
    }, [mode, token, page])

    // Fetch cash flow data
    useEffect(() => {
        if (mode === 'hello' && token) {
            setCashFlowLoading(true)
            fetch(`${API}/api/cash-flow`, {
                headers: { Authorization: `Bearer ${token}` }
            })
                .then(r => r.json())
                .then(data => {
                    setCashFlow(data)
                    setCashFlowLoading(false)
                })
                .catch(() => {
                    setCashFlow(null)
                    setCashFlowLoading(false)
                })
        }
    }, [mode, token])

    // AI Chat function
    function askAI(e) {
        e.preventDefault()
        if (!aiQuestion.trim()) return
        
        setAiLoading(true)
        setAiResponse('')
        
        fetch(`${API}/api/ai-chat`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: aiQuestion })
        })
            .then(r => r.json())
            .then(data => {
                setAiLoading(false)
                setAiResponse(data.response || 'Sorry, I could not process your request.')
            })
            .catch(err => {
                setAiLoading(false)
                setAiResponse('Error connecting to AI advisor. Please try again.')
            })
    }

    if (mode === 'hello') {
        return (
            <div style={cardStyle}>
                <h1 style={{ color: '#0b5cff', marginBottom: 24 }}>{message}</h1>
                <div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
                    <button style={buttonStyle} onClick={logout}>Sign Out</button>
                    <button 
                        style={{...buttonStyle, background: showChat ? '#666' : '#28a745'}} 
                        onClick={() => setShowChat(!showChat)}
                    >
                        {showChat ? 'Hide AI Coach' : '💬 AI Coach'}
                    </button>
                </div>

                {/* AI Chat Interface */}
                {showChat && (
                    <div style={{ 
                        marginBottom: 24, 
                        padding: 20, 
                        background: '#f0f8ff', 
                        borderRadius: 8,
                        border: '2px solid #0b5cff'
                    }}>
                        <h3 style={{ color: '#0b5cff', marginTop: 0, marginBottom: 12 }}>
                            💡 Ask Your AI Financial Coach
                        </h3>
                        <p style={{ fontSize: 14, color: '#555', marginBottom: 16 }}>
                            Get personalized, judgment-free financial advice based on your transactions.
                        </p>
                        <form onSubmit={askAI}>
                            {/* <input 
                                style={{...inputStyle, marginBottom: 12}}
                                placeholder="e.g., How can I save $100 this month?"
                                value={aiQuestion}
                                onChange={e => setAiQuestion(e.target.value)}
                                disabled={aiLoading}
                            /> */}
                            <button 
                                type="submit" 
                                style={{...buttonStyle, background: '#28a745', width: '100%'}}
                                disabled={aiLoading || !aiQuestion.trim()}
                            >
                                {aiLoading ? 'Thinking...' : 'Generate Budget Plan'}
                            </button>
                        </form>
                        {aiLoading && (
                            <div style={{ marginTop: 16, color: '#0b5cff', fontStyle: 'italic' }}>
                                ✨ Analyzing your transactions and preparing advice...
                            </div>
                        )}
                        {aiResponse && (
                            <div style={{ 
                                marginTop: 16, 
                                padding: 16, 
                                background: '#fff', 
                                borderRadius: 8,
                                border: '1px solid #ddd',
                                whiteSpace: 'pre-wrap'
                            }}>
                                <strong style={{ color: '#28a745', display: 'block', marginBottom: 8 }}>
                                    💬 AI Advisor:
                                </strong>
                                {aiResponse}
                            </div>
                        )}
                    </div>
                )}

                {/* Cash Flow Summary */}
                {cashFlowLoading ? (
                    <div style={{ textAlign: 'center', padding: '20px', color: '#888' }}>
                        Loading cash flow...
                    </div>
                ) : cashFlow && (
                    <div style={{ 
                        display: 'flex', 
                        gap: 16, 
                        marginBottom: 24,
                        justifyContent: 'space-around',
                        flexWrap: 'wrap'
                    }}>
                        <div style={{
                            flex: 1,
                            minWidth: 200,
                            padding: 20,
                            background: '#e8f5e9',
                            borderRadius: 8,
                            border: '2px solid #4caf50',
                            textAlign: 'center'
                        }}>
                            <div style={{ fontSize: 14, color: '#2e7d32', fontWeight: 600, marginBottom: 8 }}>
                                💰 INFLOW
                            </div>
                            <div style={{ fontSize: 28, color: '#1b5e20', fontWeight: 700 }}>
                                ${cashFlow.inflow.toFixed(2)}
                            </div>
                        </div>
                        <div style={{
                            flex: 1,
                            minWidth: 200,
                            padding: 20,
                            background: '#ffebee',
                            borderRadius: 8,
                            border: '2px solid #f44336',
                            textAlign: 'center'
                        }}>
                            <div style={{ fontSize: 14, color: '#c62828', fontWeight: 600, marginBottom: 8 }}>
                                💸 OUTFLOW
                            </div>
                            <div style={{ fontSize: 28, color: '#b71c1c', fontWeight: 700 }}>
                                ${cashFlow.outflow.toFixed(2)}
                            </div>
                        </div>
                        <div style={{
                            flex: 1,
                            minWidth: 200,
                            padding: 20,
                            background: cashFlow.net >= 0 ? '#e3f2fd' : '#fff3e0',
                            borderRadius: 8,
                            border: `2px solid ${cashFlow.net >= 0 ? '#2196f3' : '#ff9800'}`,
                            textAlign: 'center'
                        }}>
                            <div style={{ fontSize: 14, color: cashFlow.net >= 0 ? '#1565c0' : '#e65100', fontWeight: 600, marginBottom: 8 }}>
                                📊 NET CASH FLOW
                            </div>
                            <div style={{ fontSize: 28, color: cashFlow.net >= 0 ? '#0d47a1' : '#bf360c', fontWeight: 700 }}>
                                {cashFlow.net >= 0 ? '+' : ''}${cashFlow.net.toFixed(2)}
                            </div>
                        </div>
                    </div>
                )}

                {/* Spending Pie Chart */}
                <SpendingPieChart token={token} />

                <div style={{ marginTop: 12 }}>
                    <h3 style={{ color: '#333', marginBottom: 8 }}>
                        Recent Transactions ({totalTx} total)
                    </h3>
                    {txLoading ? (
                        <div style={{ color: '#888' }}>Loading transactions...</div>
                    ) : transactions.length === 0 ? (
                        <div style={{ padding: 16, background: '#f5f5f5', borderRadius: 8 }}>
                            <p style={{ margin: 0, color: '#666' }}>No transactions found.</p>
                        </div>
                    ) : (
                        <>
                            <div style={{ marginBottom: 12 }}>
                                {transactions.map((tx, idx) => (
                                    <div key={tx.transaction_id} style={{
                                        padding: 12,
                                        marginBottom: 8,
                                        background: '#f9f9f9',
                                        borderRadius: 8,
                                        border: '1px solid #e0e0e0'
                                    }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
                                            <span style={{ fontWeight: 600, color: '#333' }}>{tx.name}</span>
                                            <span style={{ fontWeight: 600, color: tx.amount > 0 ? '#d32f2f' : '#388e3c' }}>
                                                {tx.amount > 0 ? "-$" + Math.abs(tx.amount).toFixed(2) : "+$" + Math.abs(tx.amount).toFixed(2)}
                                            </span>
                                        </div>
                                        <div style={{ fontSize: 13, color: '#666' }}>
                                            <div>{tx.date}</div>
                                            {tx.merchant_name && <div>Merchant: {tx.merchant_name}</div>}
                                            {tx.category && <div>Category: {tx.category}</div>}
                                        </div>
                                    </div>
                                ))}
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                <button 
                                    style={{...buttonStyle, opacity: hasPrev ? 1 : 0.5}} 
                                    onClick={() => setPage(page - 1)} 
                                    disabled={!hasPrev || txLoading}
                                >
                                    ← Previous
                                </button>
                                <span style={{ color: '#666', fontSize: 14 }}>
                                    Page {page}
                                </span>
                                <button 
                                    style={{...buttonStyle, opacity: hasNext ? 1 : 0.5}} 
                                    onClick={() => setPage(page + 1)} 
                                    disabled={!hasNext || txLoading}
                                >
                                    Next →
                                </button>
                            </div>
                        </>
                    )}
                </div>
            </div>
        )
    }

    return (
        <div style={cardStyle}>
            <h2 style={{ color: '#0b5cff', marginBottom: 16 }}>{mode === 'login' ? 'Login' : 'Register'}</h2>
            <form onSubmit={mode === 'login' ? doLogin : doRegister}>
                <label style={{ fontWeight: 500 }}>Username</label>
                <input style={inputStyle} value={username} onChange={e => setUsername(e.target.value)} autoFocus />
                <label style={{ fontWeight: 500 }}>Password</label>
                <input style={inputStyle} type="password" value={password} onChange={e => setPassword(e.target.value)} />
                <div style={{ marginTop: 18, display: 'flex', alignItems: 'center' }}>
                    <button type="submit" style={buttonStyle} disabled={loading}>{mode === 'login' ? 'Login' : 'Register'}</button>
                    <button type="button" style={switchStyle} onClick={() => { setMode(mode === 'login' ? 'register' : 'login'); setError(''); setSuccess(''); }}>
                        {mode === 'login' ? 'Switch to Register' : 'Switch to Login'}
                    </button>
                </div>
            </form>
            {loading && <div style={{ marginTop: 16, color: '#888' }}>Loading...</div>}
            {error && <div style={{ marginTop: 16, color: '#d32f2f', fontWeight: 500 }}>{error}</div>}
            {success && <div style={{ marginTop: 16, color: '#388e3c', fontWeight: 500 }}>{success}</div>}
            <p style={{ marginTop: 24, color: '#555', fontSize: 14 }}>
                Credentials are stored in SQLite and a simple token is used for authentication.<br />
                <span style={{ color: '#0b5cff' }}>Budget Ally Demo</span>
            </p>
        </div>
    )
}

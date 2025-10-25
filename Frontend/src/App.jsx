import React, { useState, useEffect } from 'react'

const API = 'http://localhost:5000'

const cardStyle = {
    maxWidth: 340,
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
    const [hasNext, setHasNext] = useState(false)
    const [hasPrev, setHasPrev] = useState(false)
    const [txLoading, setTxLoading] = useState(false)

    useEffect(() => {
        if (mode === 'hello' && token) {
            setTxLoading(true)
            fetch(`${API}/api/transactions?page=${page}&per_page=10`, {
                headers: { Authorization: `Bearer ${token}` }
            })
                .then(r => r.json())
                .then(data => {
                    setTransactions(data.transactions || [])
                    setHasNext(data.has_next)
                    setHasPrev(data.has_prev)
                    setTxLoading(false)
                })
                .catch(() => {
                    setTransactions([])
                    setHasNext(false)
                    setHasPrev(false)
                    setTxLoading(false)
                })
        }
    }, [mode, token, page])

    if (mode === 'hello') {
        return (
            <div style={cardStyle}>
                <h1 style={{ color: '#0b5cff', marginBottom: 24 }}>{message}</h1>
                <div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
                    <button style={buttonStyle} onClick={logout}>Sign Out</button>
                </div>
                <div style={{ marginTop: 12 }}>
                    <h3 style={{ color: '#333', marginBottom: 8 }}>Recent Transactions</h3>
                    {txLoading ? (
                        <div style={{ color: '#888' }}>Loading transactions...</div>
                    ) : transactions.length === 0 ? (
                        <div style={{ color: '#888' }}>No transactions found.</div>
                    ) : (
                        <ul style={{ padding: 0, listStyle: 'none' }}>
                            {transactions.map(tx => (
                                <li key={tx.transaction_id} style={{ marginBottom: 10, borderBottom: '1px solid #eee', paddingBottom: 6 }}>
                                    <b>{tx.name}</b> <span style={{ color: '#888' }}>({tx.date})</span><br />
                                    <span>Amount: <b>${tx.amount}</b></span><br />
                                    <span>Account: <b>{tx.account_id}</b></span>
                                    {tx.merchant_name && <span><br />Merchant: {tx.merchant_name}</span>}
                                    {tx.category && <span><br />Category: {tx.category}</span>}
                                </li>
                            ))}
                        </ul>
                    )}
                    <div style={{ display: 'flex', gap: 12, marginTop: 12 }}>
                        <button style={buttonStyle} onClick={() => setPage(page - 1)} disabled={!hasPrev || txLoading}>Previous</button>
                        <button style={buttonStyle} onClick={() => setPage(page + 1)} disabled={!hasNext || txLoading}>Next</button>
                    </div>
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

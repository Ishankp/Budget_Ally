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

    // Transaction count state
    const [txCount, setTxCount] = useState(0)
    const [txLoading, setTxLoading] = useState(false)

    useEffect(() => {
        if (mode === 'hello' && token) {
            setTxLoading(true)
            fetch(`${API}/api/transactions?page=1&per_page=1000`, {
                headers: { Authorization: `Bearer ${token}` }
            })
                .then(r => r.json())
                .then(data => {
                    setTxCount(data.total || 0)
                    setTxLoading(false)
                })
                .catch(() => {
                    setTxCount(0)
                    setTxLoading(false)
                })
        }
    }, [mode, token])

    if (mode === 'hello') {
        return (
            <div style={cardStyle}>
                <h1 style={{ color: '#0b5cff', marginBottom: 24 }}>{message}</h1>
                <div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
                    <button style={buttonStyle} onClick={logout}>Sign Out</button>
                </div>
                <div style={{ marginTop: 12 }}>
                    <h3 style={{ color: '#333', marginBottom: 8 }}>Transactions in Database</h3>
                    {txLoading ? (
                        <div style={{ color: '#888' }}>Checking database...</div>
                    ) : (
                        <div style={{ padding: 16, background: '#f5f5f5', borderRadius: 8, marginBottom: 12 }}>
                            <p style={{ margin: 0, fontSize: 18, fontWeight: 600, color: '#333' }}>
                                {txCount} transaction{txCount !== 1 ? 's' : ''} found in database
                            </p>
                            {txCount > 0 && (
                                <p style={{ margin: '8px 0 0', color: '#666', fontSize: 14 }}>
                                    ✓ Data successfully stored from Plaid sandbox
                                </p>
                            )}
                        </div>
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

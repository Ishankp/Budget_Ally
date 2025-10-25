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

	if (mode === 'hello') {
		// Move Plaid state/hooks outside to avoid re-initialization
		const [plaidLinked, setPlaidLinked] = useState(false)
		const [balances, setBalances] = useState(null)
		const [plaidError, setPlaidError] = useState('')
		const [plaidLoading, setPlaidLoading] = useState(false)

		async function connectPlaid() {
			setPlaidError('')
			setPlaidLoading(true)
			// Step 1: get link token
			try {
				const res = await fetch(`${API}/api/plaid/link_token`, {
					method: 'POST',
					headers: { Authorization: `Bearer ${token}` },
				})
				const body = await res.json()
				if (!res.ok || !body.link_token) {
					setPlaidError(body.error || 'Could not get link token')
					setPlaidLoading(false)
					return
				}
				// Step 2: open Plaid Link (demo: just simulate success)
				// In production, use Plaid Link SDK. Here, simulate linking and call exchange endpoint.
				// For demo, prompt for public_token
				const public_token = window.prompt('Enter Plaid public_token (sandbox):', '')
				if (!public_token) {
					setPlaidError('No public_token entered')
					setPlaidLoading(false)
					return
				}
				const exchRes = await fetch(`${API}/api/plaid/exchange_public_token`, {
					method: 'POST',
					headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
					body: JSON.stringify({ public_token }),
				})
				const exchBody = await exchRes.json()
				if (!exchRes.ok) {
					setPlaidError(exchBody.error || 'Could not exchange token')
					setPlaidLoading(false)
					return
				}
				setPlaidLinked(true)
				// Step 3: fetch balances
				const balRes = await fetch(`${API}/api/plaid/balance`, {
					headers: { Authorization: `Bearer ${token}` },
				})
				const balBody = await balRes.json()
				if (balRes.ok && balBody.accounts) {
					setBalances(balBody.accounts)
				} else {
					setPlaidError(balBody.error || 'Could not fetch balances')
				}
			} catch (err) {
				setPlaidError('Plaid connection failed')
			}
			setPlaidLoading(false)
		}

		return (
			<div style={cardStyle}>
				<h1 style={{ color: '#0b5cff', marginBottom: 24 }}>{message}</h1>
				<div style={{ display: 'flex', gap: 12, marginBottom: 24 }}>
					<button style={buttonStyle} onClick={logout}>Logout</button>
					<button style={buttonStyle} onClick={connectPlaid} disabled={plaidLoading || plaidLinked}>
						{plaidLinked ? 'Plaid Connected' : 'Connect to Plaid'}
					</button>
				</div>
				{plaidLoading && <div style={{ color: '#888', marginTop: 12 }}>Connecting to Plaid...</div>}
				{plaidLinked && balances && (
					<div>
						<h3 style={{ color: '#388e3c' }}>Plaid Linked!</h3>
						<div style={{ marginTop: 12 }}>
							<h4>Account Balances:</h4>
							<ul>
								{balances.map(acc => (
									<li key={acc.account_id}>
										<b>{acc.name}</b>: ${acc.balances.current} ({acc.type})
									</li>
								))}
							</ul>
						</div>
					</div>
				)}
				{plaidError && <div style={{ color: '#d32f2f', marginTop: 12 }}>{plaidError}</div>}
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

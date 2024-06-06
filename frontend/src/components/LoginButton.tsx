// src/components/LoginButton.tsx

import axios from 'axios';
import { useState } from 'react';

const LoginButton: React.FC = () => {
    const [message, setMessage] = useState<string>('');
    const [userInfo, setUserInfo] = useState<any>(null);

    const handleLogin = async () => {
        try {
            const response = await axios.get(
                'http://localhost:5000/login',
                { withCredentials: true}
            );
            const { auth_url } = response.data;
            console.log( auth_url )

            // Redirect the user to the auth URL
            window.location.href = auth_url;
        } catch (error) {
            console.error('Error during login:', error);
            setMessage('Login failed');
        }
    };

    const getUserInfo = async() => {
        try {
            const response = await axios.get(
                'http://localhost:5000/me',
                { withCredentials: true}
            );
            setUserInfo(response.data)
        }
        catch (error) {
            console.error('Error getting user info:', error)
        }
    };

    return (
        <div>
            <button onClick={handleLogin}>Login</button>
            <button onClick={getUserInfo}>Get User Info</button>
            {message && <p>{message}</p>}
            {userInfo && (
                <div>
                        <h3>User Info</h3>
                        <p>Name: {userInfo.display_name}</p>
                        <p>Email: {userInfo.email}</p>
                </div>
            )}
        </div>
    );
};

export default LoginButton;

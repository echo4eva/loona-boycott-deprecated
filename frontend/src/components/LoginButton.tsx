// src/components/LoginButton.tsx
import { Button } from "@/components/ui/button";
import axios from 'axios';
import { useState } from 'react';

const LoginButton: React.FC = () => {
    const [userInfo, setUserInfo] = useState<any>(null);

    const handleLogin = async () => {
        try {
            const response = await axios.get(
                'http://127.0.0.1:5000/login',
                { withCredentials: true }
            );
            const { auth_url } = response.data;
            console.log( auth_url )

            // Redirect the user to the auth URL
            window.location.href = auth_url;
        } catch (error) {
            console.error('Error during login:', error);
        }
    };

    return (
        <div>
            <Button onClick={handleLogin}>Login</Button>
        </div>
    );
};

export default LoginButton;

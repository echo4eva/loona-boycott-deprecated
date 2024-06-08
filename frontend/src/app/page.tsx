// src/app/page.tsx
'use client'
import Image from "next/image";
import LoginButton from "@/components/LoginButton";
import axios from "axios";
import { PlaylistForm }  from "@/components/PlaylistForm";
import { useEffect, useState } from "react";
import { User } from "@/types";

export default function Home() {

  const [userInfo, setUserInfo] = useState<User | null>(null);

  // Checks if user is authenticated or not
  useEffect(() => {
    (async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/me",
          { withCredentials: true }
        );
        // If authenticated, then grab user info
        setUserInfo(response.data)
        console.log(userInfo)
      } catch (error) {
        console.log("Not authenticated")
      }
    })(); // Runs IIFE: https://developer.mozilla.org/en-US/docs/Glossary/IIFE
  }, []); //

  return (
    <main className="flex min-h-screen flex-col items-center space-y-5 p-24">
      <header className="flex flex-col items-center">
        <h1>Loona Boycott</h1>
        <h5>replaces your official streams with episodes</h5>
      </header>
      {userInfo != null ? (
        <p>hi {userInfo.display_name}!</p>
      )
      :
      (
        <LoginButton />
      )}
      <PlaylistForm />
    </main>
  );
}
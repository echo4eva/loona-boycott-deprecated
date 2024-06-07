'use client'
import Image from "next/image";
import LoginButton from "@/components/LoginButton";
import { PlaylistForm }  from "@/components/PlaylistForm";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>Loona Boycott</h1>
      <LoginButton />
      <PlaylistForm />
    </main>
  );
}
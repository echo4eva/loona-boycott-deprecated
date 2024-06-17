"use client"
/* form boilerplate
https://ui.shadcn.com/docs/components/form
https://zod.dev/ */
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import axios from "axios"

// form components
import { Button } from "@/components/ui/button"
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { useState } from "react"


// validates if correct if it's a playlist url
function isValidUrl(url: string): boolean {
    try {
        const baseSpotifyURL = 'https://open.spotify.com/playlist/';
        const parsedUrl = new URL(url);

        console.log(parsedUrl.origin)

        return parsedUrl.origin + "/playlist/" === baseSpotifyURL;
    } catch (error) {
        return false;
    }
}

// schema/blueprint for validation
const formSchema = z.object ({
    playlist: z.string().url().refine((playlist) => isValidUrl(playlist), {
        message: "Invalid url",
    }),
});

// take apart 
function extractId(playlist_url: string): string | null {
    const regex = /playlist\/(.*?)\?/;
    const match = playlist_url.match(regex);
    return match ? match[1] : null;
}

interface MessageComponentProps {
  message: string;
  status: int;
}

export function PlaylistForm() {

    const [status, setStatus] = useState<number>(0);
    const [message, setMessage] = useState<string>("");

    const handleOnSubmit = async (values: z.infer<typeof formSchema>) => {
        try {
            const response = await axios.post(
                'http://127.0.0.1:5000/boycott', {
                     playlist_id: extractId(values.playlist)
                }, {
                    withCredentials: true,
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                },
            );
            console.log('success:', response);
            setMessage(response.data.message);
            console.log(response.status);
            setStatus(response.status);
            console.log(status);
        } catch (error) {
            console.error('Error during submission:', error);
            setMessage(error.message);
            setStatus(false);
        }
    };

    // creates the form
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),  // integrate validation from zod
        defaultValues: {
            playlist: "",
        },
    })

    // test function for extracting, works!
    function onSubmit(values: z.infer<typeof formSchema>) {
        console.log(extractId(values.playlist))
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(handleOnSubmit)} className="space-y-8 w-[55%]">
                <FormField 
                    control={form.control}
                    name="playlist"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Playlist</FormLabel>
                            <FormControl>
                                <Input placeholder="Spotify Playlist URL" {...field} />
                            </FormControl>
                            <FormDescription>
                                {message == "" ? (<>Put the playlist to convert above!</>) : (<>{message}</>)} 
                            </FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />
            <Button type="submit">Submit</Button>
            </form>
        </Form>
    )
}

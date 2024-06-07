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

// schema/blueprint for validation
const formSchema = z.object ({
    playlist: z.string().url({
        message: "Invalid url",
    }),
})

// take apart 
function extractId(playlist_url: string): string | null {
    const regex = /playlist\/(.*?)\?/;
    const match = playlist_url.match(regex);
    return match ? match[1] : null;
}

export function PlaylistForm() {

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
            console.log( values )

        } catch (error) {
            console.error('Error during submission:', error);
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
                                Put the playlist to convert here!
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
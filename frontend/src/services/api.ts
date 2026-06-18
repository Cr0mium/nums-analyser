export async function uploadFile(file: File) {
    const formData = new FormData();

    formData.append("file", file);
    // formData.append("query", query);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "post",
        body: formData,
    });

    // const response = await fetch("http://127.0.0.1:8000/", {
    //     method: "get",
    // });

    if (!response.ok) {
        throw new Error("Upload failed");
    }

    return response.json();
}

export async function sendMessage(sessionId: string, message: string) {
    console.log(sessionId, message)
    const response = await fetch("http://127.0.0.1:8000/chat", {

        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            session_id: sessionId,
            message: message,
        }),
    });

    if (!response.ok) {
        console.log(await response.json());
        throw new Error("Message failed");
    }

    return response.json();
}

export async function uploadFile(file: File, query: string) {
    const formData = new FormData();

    formData.append("file", file);
    formData.append("query", query);

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

import { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import "../styles/ChatBox.css";
import { sendMessage } from "../services/api"
interface Message {
    role: "user" | "assistant";
    content: string;
}
interface ChatBoxProps {

    sessionId: string | null;

}

function ChatBox({ sessionId }: ChatBoxProps) {
    const [input, setInput] = useState<string>("");

    const [messages, setMessages] = useState<Message[]>([
        {
            role: "assistant",
            content:
                "Your dataset is loaded. Ask me anything about trends, correlations, anomalies, or specific columns."
        }
    ]);

    // For "Thinking..." state
    const [isLoading, setIsLoading] = useState<boolean>(false);

    // Reference to bottom of chat
    const messagesEndRef = useRef<HTMLDivElement | null>(null);

    // Auto scroll whenever messages/loading changes
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages, isLoading]);

    async function handleSend() {
        if (!input.trim()) return;

        // Add user message
        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: input
            }
        ]);

        setInput("");

        // Show thinking bubble
        setIsLoading(true);

        // Simulate backend response
        try {
            const data = await sendMessage(sessionId, input);
            // console.log(data)
            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content: data.response,
                },
            ]);
        } catch (error) {
            console.error(error);
        }
        finally {
            setIsLoading(false);
        }
    }

    return (
        <div className="chat-box">

            <div className="messages">

                {messages.map((message, index) => (
                    <div
                        className={`message ${message.role}`}
                        key={index}
                    >
                        <ReactMarkdown>
                            {message.content}
                        </ReactMarkdown>
                    </div>
                ))}

                {isLoading && (
                    <div className="message assistant">
                        Thinking...
                    </div>
                )}

                {/* Used for auto scroll */}
                <div ref={messagesEndRef}></div>

            </div>

            <div className="input-area">

                <textarea
                    placeholder="Ask something about your data..."
                    value={input}
                    onChange={(event) => {
                        setInput(event.target.value);
                    }}
                    onKeyDown={(event) => {
                        if (event.key === "Enter" && !event.shiftKey) {
                            event.preventDefault();
                            handleSend();
                        }
                    }}
                />

                <button
                    disabled={!input.trim() || isLoading}
                    onClick={handleSend}
                >
                    Send
                </button>

            </div>

        </div>
    );
}

export default ChatBox;

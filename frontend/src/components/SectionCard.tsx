interface SectionCardProps{
    title: string,
    children: React.ReactNode
}

function SectionCard({ title, children }: SectionCardProps) {
    return (
            <div
                style={{
                    border: "1px solid #ccc",
                    borderRadius: "10px",
                    padding: "16px",
                    marginBottom: "20px",
                }}
            >
                <h3>{title}</h3>
    
                {children}
            </div>
        );
}

export default SectionCard;
interface SectionCardProps {
    title: string;
    children: React.ReactNode;
}

function SectionCard({ title, children }: SectionCardProps) {
    return (
        <div>
            <h3>{title}</h3>

            {children}
        </div>
    );
}

export default SectionCard;

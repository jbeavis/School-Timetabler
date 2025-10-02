
function ListGroup() {
    const items = [
        'London',
        'New York',
        'Tokyo',
        'Berlin',
        'Paris'
    ]
    return (
        <>
            <h1>List</h1>
            <ul className="list-group">
                {items.map(item => <li key={item} className="list-group-item">{item}</li>)}
            </ul>
        </>
    );
}

export default ListGroup;   
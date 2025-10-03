
function ListGroup() {
    const items = [
        'London',
        'New York',
        'Tokyo',
        'Berlin',
        'Paris'
    ];
    if (items.length == 0) 
        return <p>No items found</p>;
    return (
        <>
            <h1>List</h1>
            <ul className="list-group">
                {items.map(item => <li key={item} className="list-group-item" onClick={() => console.log(item)}>{item}</li>)}
            </ul>
        </>
    );
}

export default ListGroup;   
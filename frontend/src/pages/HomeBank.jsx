import { useEffect, useState, useCallback } from "react";
import axios from "axios"
import { fetchMovements } from "../api/movements";
import MovementList from "../components/MovementList";


function HomeBank() {
    const [movements, setMovements] = useState([])
    const [firstLoad,setFirstLoad] = useState(true)

    const loadMovements = useCallback(async () => {
        const res = await fetchMovements();
        console.log("movements",res.data)
        setMovements(res.data)
    }, []);

    let contentMovements = <p>No data..</p>;
    if (movements.length>0){
        contentMovements=<MovementList movements={movements} />
    }else if (firstLoad){
        setFirstLoad(false)
        loadMovements()
    }
    
    return (
        <>
            <h1>Home Bank</h1>
            <div>
                {contentMovements}
            </div>
        </>
    );
}

export default HomeBank;
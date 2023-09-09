import { useNavigate } from "react-router-dom";
// import { updateTask } from "../api/tasks";

function MovementCard({ movement }) {
    return (
        <div>
            <h3>Moviment</h3>
            <p>{movement.description}</p>
        </div>
    )
}

export default MovementCard
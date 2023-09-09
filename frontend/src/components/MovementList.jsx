import MovementCard from "./MovementCard";

function MovementList({ movements }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {
        movements.map((movement) => {
          return <MovementCard key={movement._id} movement={movement} />
        })
      }
    </div>
  );
}

export default MovementList;
import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  return (
    <header className="flex justify-between items-center my-7">
      <Link to="/">
        <h1 className="text-3xl font-bold">EnGuillem.com</h1>
      </Link>
      {location.pathname === "/" ? (
        <Link
          to="/bank/home"
          className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
        >
          Bank app
        </Link>
      ) : (
        <Link
          to="/"
          className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
        >
          back
        </Link>
      )}
    </header>
  );
}

export default Navbar;
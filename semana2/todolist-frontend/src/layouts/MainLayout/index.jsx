import { useSelector } from "react-redux";
import { Navigate, Outlet } from "react-router-dom";
import { selectorUser } from "../../selectors/userSelector";

export default function MainLayout() {
  // const user = useSelector((state) => state.user.data);
  const user = useSelector(selectorUser);

  if (!user) return <Navigate to="signup" />;

  return (
    <>
      <nav className="bg-blue-700 flex justify-end gap-5 pe-5 py-3">
        <img src={user.avatar} alt="" width={40} className="rounded-full" />
        <div className="text-sm text-white">
          <p>
            {user.name} {user.lastname}
          </p>
          <p>{user.email}</p>
        </div>
      </nav>
      <Outlet />
    </>
  );
}

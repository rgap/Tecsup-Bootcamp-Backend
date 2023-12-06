import { useSelector } from "react-redux";
import { Navigate, Outlet } from "react-router-dom";
import { selectorUser } from "../../selectors/userSelector";

export default function AuthLayout() {
  const user = useSelector(selectorUser);

  if (user) return <Navigate to="/" />;

  return (
    <>
      <Outlet />
    </>
  );
}

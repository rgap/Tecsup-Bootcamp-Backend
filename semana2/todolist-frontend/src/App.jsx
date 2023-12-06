import { Provider } from "react-redux";
import Router from "./router";
import { store } from "./store";

export default function App() {
  // mediante provider, store comparte todas las variables que tiene con router
  return (
    <Provider store={store}>
      <Router />
    </Provider>
  );
}

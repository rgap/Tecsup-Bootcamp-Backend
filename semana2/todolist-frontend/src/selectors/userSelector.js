import { createSelector } from "@reduxjs/toolkit";

// const user = useSelector((state) => state.user.data);
const globalState = (state) => state;

// destructuration
// createSelector receives globalState and extracts {user} from it
export const selectorUser = createSelector(
  globalState,
  ({ user }) => user.data
);
export const selectorUserId = createSelector(
  globalState,
  ({ user }) => user.data.id
);

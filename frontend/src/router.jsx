import {
    Navigate,
    Route,
    createBrowserRouter,
    createRoutesFromElements,
  } from "react-router-dom";
  import Home from "./pages/Home.jsx";
  import Login from "./pages/Login.jsx";
  import Layout from "./pages/Layout.jsx";
  import UserSelect from "./pages/UserSelect.jsx";
  import Protected from "./pages/Protected.jsx";
  
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path="/" element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="user-select" element={<UserSelect />} />
          <Route path="login" element={<Login />} />
          <Route path="protected" element={<Protected />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Route>
      </>
    ),
    // { basename: import.meta.env.DEV ? "/" : "/react-face-auth/" }
    { basename: "/" }
  );
  
  export default router;
  
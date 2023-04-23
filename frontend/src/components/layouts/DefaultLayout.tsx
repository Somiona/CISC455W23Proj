import { default as c } from "classnames";
import Meta from "components/essential/Meta";

// import { Footer, Header } from "components/essential/";
import { FCwCC } from "utils/BetterFC";

const DefaultLayout: FCwCC = ({ children, className }) => {
  return (
    <>
      <Meta />
      {/* <Header /> */}
      <main className={c("app-layout-main", className)}>{children}</main>
      {/* <Footer /> */}
    </>
  );
};

export default DefaultLayout;

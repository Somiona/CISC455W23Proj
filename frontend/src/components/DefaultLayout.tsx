// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import { default as c } from "classnames";
import Meta from "components/Meta";
import { Open_Sans } from "next/font/google";

// import { Footer, Header } from "components/essential/";
import { FCwCC } from "utils/BetterFC";
import SideNav, { PossiblePages } from "./SideNav";
import NavBar from "./NavBar";
import { prop } from "ramda";

// eslint-disable-next-line no-unused-vars
const open_sans = Open_Sans({
  subsets: ["latin"],
  weight: ["300", "400", "600", "700"],
  variable: "--font-open-sans",
});

const app_cls = c(
  open_sans.className,
  "app m-0 text-base font-normal dark:bg-slate-900 leading-default bg-gray-50 text-slate-500"
);

const DefaultLayout: FCwCC<{ pageName: PossiblePages }> = (props) => {
  return (
    <>
      <Meta />
      {/* <Header /> */}
      <div className={app_cls}>
        <div className="absolute w-full bg-blue-500 dark:hidden min-h-75"></div>
        <SideNav currentActivate={props.pageName} />
        <main
          className={c(
            "app-layout-main relative h-full max-h-screen transition-all duration-200 ease-in-out xl:ml-68 rounded-xl",
            props.className
          )}
        >
          <NavBar pageName={props.pageName} />
          {props.children}
        </main>
      </div>
      {/* <Footer /> */}
    </>
  );
};

export default DefaultLayout;

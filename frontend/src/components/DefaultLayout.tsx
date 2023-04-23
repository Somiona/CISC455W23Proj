import { default as c } from "classnames";
import Meta from "components/Meta";
import { Open_Sans } from "next/font/google";

// import { Footer, Header } from "components/essential/";
import { FCwCC } from "utils/BetterFC";
import Side from "./SideNav";

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

const DefaultLayout: FCwCC = ({ children, className }) => {
  return (
    <>
      <Meta />
      {/* <Header /> */}
      <div className={app_cls}>
        <div className="absolute w-full bg-blue-500 dark:hidden min-h-75"></div>
        <Side />
        <main className={c("app-layout-main", className)}>{children}</main>
      </div>
      {/* <Footer /> */}
    </>
  );
};

export default DefaultLayout;

// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import { FC } from "react";
import { appConfig } from "utils/config";
import Link from "next/link";
import favicon from "../../public/favicon-64.png";
import Image from "next/image";

import { faTv, faTable, faUser } from "@fortawesome/free-solid-svg-icons";
import SideNavItem from "./SideNavItem";

type PossiblePages = "Dashboard" | "Tables" | "Individuals";

export type { PossiblePages };

const SideNav: FC<{ currentActivate: PossiblePages }> = (prop) => {
  return (
    <aside
      className="fixed inset-y-0 flex-wrap items-center justify-between block w-full p-0 my-4
                overflow-y-auto antialiased transition-transform duration-200 -translate-x-full bg-white border-0 shadow-xl
                dark:shadow-none dark:bg-slate-850 max-w-64 ease-nav-brand z-990 xl:ml-6 rounded-2xl xl:left-0 xl:translate-x-0"
    >
      <div className="h-19">
        <i
          className="absolute top-0 right-0 p-4 opacity-50 cursor-pointer fas fa-times dark:text-white text-slate-400 xl:hidden"
          sidenav-close="true"
        ></i>
        <Link
          className="block px-8 py-6 m-0 text-sm whitespace-nowrap dark:text-white text-slate-700"
          href="/"
        >
          <Image
            alt="Main Logo"
            src={favicon}
            width={64}
            height={64}
            className="inline h-full max-w-10 transition-all duration-200 ease-nav-brand max-h-10"
          />
          <span className="ml-1 font-semibold transition-all duration-200 ease-nav-brand">
            {appConfig.site_name}
          </span>
        </Link>
      </div>

      <hr className="h-px mt-0 bg-transparent bg-gradient-to-r from-transparent via-black/40 to-transparent dark:bg-gradient-to-r dark:from-transparent dark:via-white dark:to-transparent" />

      <div className="items-center block w-auto max-h-screen overflow-auto h-sidenav grow basis-full">
        <ul className="flex flex-col pl-0 mb-0">
          <SideNavItem
            faicon={faTv}
            tag="Dashboard"
            href="/"
            isActive={prop.currentActivate === "Dashboard"}
            className="text-blue-500"
            key={1}
          />
          <SideNavItem
            faicon={faTable}
            tag="Tables"
            href="/tables"
            isActive={prop.currentActivate === "Tables"}
            className="text-orange-500"
            key={2}
          />
          <SideNavItem
            faicon={faUser}
            tag="Individuals"
            href="/individuals"
            isActive={prop.currentActivate === "Individuals"}
            className="text-emerald-500"
            key={3}
          />

          {/* <li className="w-full mt-4">
            <h6 className="pl-6 ml-2 text-xs font-bold leading-tight uppercase dark:text-white opacity-60">
              Account pages
            </h6>
          </li>

          <li className="mt-0.5 w-full">
            <a
              className=" dark:text-white dark:opacity-80 py-2.7 text-sm ease-nav-brand my-0 mx-2 flex items-center whitespace-nowrap px-4 transition-colors"
              href="./pages/profile.html"
            >
              <div className="mr-2 flex h-8 w-8 items-center justify-center rounded-lg bg-center stroke-0 text-center xl:p-2.5">
                <i className="relative top-0 text-sm leading-normal text-slate-700 ni ni-single-02"></i>
              </div>
              <span className="ml-1 duration-300 opacity-100 pointer-events-none ease">
                Profile
              </span>
            </a>
          </li>

          <li className="mt-0.5 w-full">
            <a
              className=" dark:text-white dark:opacity-80 py-2.7 text-sm ease-nav-brand my-0 mx-2 flex items-center whitespace-nowrap px-4 transition-colors"
              href="./pages/sign-in.html"
            >
              <div className="mr-2 flex h-8 w-8 items-center justify-center rounded-lg bg-center stroke-0 text-center xl:p-2.5">
                <i className="relative top-0 text-sm leading-normal text-orange-500 ni ni-single-copy-04"></i>
              </div>
              <span className="ml-1 duration-300 opacity-100 pointer-events-none ease">
                Sign In
              </span>
            </a>
          </li>

          <li className="mt-0.5 w-full">
            <a
              className=" dark:text-white dark:opacity-80 py-2.7 text-sm ease-nav-brand my-0 mx-2 flex items-center whitespace-nowrap px-4 transition-colors"
              href="./pages/sign-up.html"
            >
              <div className="mr-2 flex h-8 w-8 items-center justify-center rounded-lg bg-center stroke-0 text-center xl:p-2.5">
                <i className="relative top-0 text-sm leading-normal text-cyan-500 ni ni-collection"></i>
              </div>
              <span className="ml-1 duration-300 opacity-100 pointer-events-none ease">
                Sign Up
              </span>
            </a>
          </li> */}
        </ul>
      </div>
    </aside>
  );
};

export default SideNav;

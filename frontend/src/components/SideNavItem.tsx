// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import Link from "next/link";
import { default as c } from "classnames";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";
import { FC } from "react";
import { FCwCC } from "utils/BetterFC";

type ISideNavItemProps = {
  faicon: IconDefinition;
  tag: string;
  href: string;
  isActive: boolean;
  className?: string;
};

const TextItem: FC<{ tag: string }> = ({ tag }) => {
  return <span className="ml-1 duration-300 opacity-100 pointer-events-none ease">{tag}</span>;
};

const IconItem: FC<{ faicon: IconDefinition; className?: string }> = ({ faicon, className }) => {
  return (
    <div className="mr-2 flex h-8 w-8 items-center justify-center rounded-lg bg-center stroke-0 text-center xl:p-2.5">
      <FontAwesomeIcon
        icon={faicon}
        className={c("relative top-0 text-sm leading-normal", className)}
      />
    </div>
  );
};

const ActiveItem: FCwCC<{ isActive: boolean; href: string }> = ({ isActive, href, children }) => {
  return (
    <Link
      className={c(
        {
          "py-2.7 bg-blue-500/13 rounded-lg font-semibold text-slate-700": isActive,
        },
        "dark:text-white dark:opacity-80 py-2.7 text-sm ease-nav-brand my-0 mx-2 flex items-center whitespace-nowrap px-4 transition-colors"
      )}
      href={href}
    >
      {children}
    </Link>
  );
};

export default function SideNavItem(prop: ISideNavItemProps) {
  return (
    <li className="mt-0.5 w-full">
      <ActiveItem isActive={prop.isActive} href={prop.href}>
        <IconItem faicon={prop.faicon} className={prop.className} />
        <TextItem tag={prop.tag} />
      </ActiveItem>
    </li>
  );
}

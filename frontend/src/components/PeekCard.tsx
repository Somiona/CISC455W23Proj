import React, { FC } from "react";
import { default as c } from "classnames";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

type IPeekCard = {
  title: string;
  main: string;
  percentage: number;
  since: string;
  bgColor: string;
  faicon: IconDefinition;
};

const IconItem: FC<{ faicon: IconDefinition; color: string }> = ({ faicon, color }) => {
  return (
    <div className={c("inline-block w-12 h-12 text-center rounded-circle", color)}>
      <FontAwesomeIcon icon={faicon} className="leading-none text-2xl relative top-3 text-white" />
    </div>
  );
};

const PeekCard: FC<IPeekCard> = (props) => {
  const p = `${props.percentage >= 0 ? "+" : ""}${Math.floor(props.percentage * 100)}%`;

  return (
    <div className="w-full max-w-full px-3 mb-6 sm:w-1/2 sm:flex-none xl:mb-0 xl:w-1/4">
      <div className="relative flex flex-col min-w-0 break-words bg-white shadow-xl dark:bg-slate-850 dark:shadow-dark-xl rounded-2xl bg-clip-border">
        <div className="flex-auto p-4">
          <div className="flex flex-row -mx-3">
            <div className="flex-none w-2/3 max-w-full px-3">
              <div>
                <p className="mb-0 font-sans text-sm font-semibold leading-normal uppercase dark:text-white dark:opacity-60">
                  {props.title}
                </p>
                <h5 className="mb-2 font-bold dark:text-white">{props.main}</h5>
                <p className="mb-0 dark:text-white dark:opacity-60">
                  <span
                    className={c("text-sm font-bold leading-normal", {
                      "text-emerald-500": props.percentage >= 0,
                      "text-red-600": props.percentage < 0,
                    })}
                  >
                    {p}
                  </span>
                  &nbsp;{props.since}
                </p>
              </div>
            </div>
            <div className="px-3 text-right basis-1/3">
              <IconItem faicon={props.faicon} color={props.bgColor} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PeekCard;

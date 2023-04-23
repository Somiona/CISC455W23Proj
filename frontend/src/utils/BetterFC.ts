import type { FC, PropsWithChildren } from "react";

type PropsWithClassName<P> = P & { className?: string };

type FunctionComponentWithChildrenAndClassName<P> = FC<PropsWithClassName<PropsWithChildren<P>>>;

//* 这个类型可以自动给 Prop 加上 className 和 children.
// eslint-disable-next-line @typescript-eslint/ban-types
type FCwCC<P = {}> = FunctionComponentWithChildrenAndClassName<P>;

export type { PropsWithClassName, FunctionComponentWithChildrenAndClassName, FCwCC };

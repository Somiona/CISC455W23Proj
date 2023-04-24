// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import DefaultLayout from "components/DefaultLayout";

export default function Home() {
  return (
    <DefaultLayout pageName="Individuals">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          This is Individuals Page
        </p>
      </div>
    </DefaultLayout>
  );
}
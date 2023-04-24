// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import DefaultLayout from "components/DefaultLayout";
import PeekCard from "components/PeekCard";
import {
  faMoneyCheckDollar,
  faUserTie,
  faFaceSadCry,
  faThumbsUp,
} from "@fortawesome/free-solid-svg-icons";

export default function Home() {
  return (
    <DefaultLayout pageName="Dashboard">
      <div className="w-full px-6 py-6 mx-auto">
        {/* row 1 */}
        <div className="flex flex-wrap -mx-3">
          {/* card1 */}
          <PeekCard
            title="Overall Price"
            main="$21000"
            percentage={0.5}
            since="since last day"
            faicon={faMoneyCheckDollar}
            bgColor="bg-gradient-to-t from-blue-500 to-violet-500"
          />

          {/* card2 */}
          <PeekCard
            title="Best Individual"
            main="Noon Kho"
            percentage={-0.3}
            since="since last day"
            faicon={faUserTie}
            bgColor="bg-gradient-to-t from-red-600 to-orange-600"
          />

          {/* card3 */}
          <PeekCard
            title="Emotional Status"
            main="Damage"
            percentage={0.8}
            since="since last day"
            faicon={faFaceSadCry}
            bgColor="bg-gradient-to-t from-emerald-500 to-teal-400"
          />

          {/* card4 */}
          <PeekCard
            title="Average Fitness"
            main="42"
            percentage={0.02}
            since="since last day"
            faicon={faThumbsUp}
            bgColor="bg-gradient-to-t from-orange-500 to-yellow-500"
          />
        </div>

        {/* cards row 2 */}
        <div className="flex flex-wrap mt-6 -mx-3">
          <div className="w-full max-w-full px-3 mt-0 lg:w-7/12 lg:flex-none">
            <div className="border-black/12.5 dark:bg-slate-850 dark:shadow-dark-xl shadow-xl relative z-20 flex min-w-0 flex-col break-words rounded-2xl border-0 border-solid bg-white bg-clip-border">
              <div className="border-black/12.5 mb-0 rounded-t-2xl border-b-0 border-solid p-6 pt-4 pb-0">
                <h6 className="capitalize dark:text-white">Sales overview</h6>
                <p className="mb-0 text-sm leading-normal dark:text-white dark:opacity-60">
                  <i className="fa fa-arrow-up text-emerald-500"></i>
                  <span className="font-semibold">4% more</span> in 2021
                </p>
              </div>
              <div className="flex-auto p-4">
                <div>
                  <canvas id="chart-line" height="300"></canvas>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* <!-- cards row 3 -->

        <div className="flex flex-wrap mt-6 -mx-3">
          <div className="w-full max-w-full px-3 mt-0 mb-6 lg:mb-0 lg:w-7/12 lg:flex-none">
            <div className="relative flex flex-col min-w-0 break-words bg-white border-0 border-solid shadow-xl dark:bg-slate-850 dark:shadow-dark-xl dark:bg-gray-950 border-black-125 rounded-2xl bg-clip-border">
              <div className="p-4 pb-0 mb-0 rounded-t-4">
                <div className="flex justify-between">
                  <h6 className="mb-2 dark:text-white">Sales by Country</h6>
                </div>
              </div>
              <div className="overflow-x-auto">
                <table className="items-center w-full mb-4 align-top border-collapse border-gray-200 dark:border-white/40">
                  <tbody>
                    <tr>
                      <td className="p-2 align-middle bg-transparent border-b w-3/10 whitespace-nowrap dark:border-white/40">
                        <div className="flex items-center px-2 py-1">
                          <div>
                            <img src="./assets/img/icons/flags/US.png" alt="Country flag" />
                          </div>
                          <div className="ml-6">
                            <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Country:</p>
                            <h6 className="mb-0 text-sm leading-normal dark:text-white">United States</h6>
                          </div>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Sales:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">2500</h6>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Value:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">$230,900</h6>
                        </div>
                      </td>
                      <td className="p-2 text-sm leading-normal align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="flex-1 text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Bounce:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">29.9%</h6>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td className="p-2 align-middle bg-transparent border-b w-3/10 whitespace-nowrap dark:border-white/40">
                        <div className="flex items-center px-2 py-1">
                          <div>
                            <img src="./assets/img/icons/flags/DE.png" alt="Country flag" />
                          </div>
                          <div className="ml-6">
                            <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Country:</p>
                            <h6 className="mb-0 text-sm leading-normal dark:text-white">Germany</h6>
                          </div>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Sales:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">3.900</h6>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Value:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">$440,000</h6>
                        </div>
                      </td>
                      <td className="p-2 text-sm leading-normal align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="flex-1 text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Bounce:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">40.22%</h6>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td className="p-2 align-middle bg-transparent border-b w-3/10 whitespace-nowrap dark:border-white/40">
                        <div className="flex items-center px-2 py-1">
                          <div>
                            <img src="./assets/img/icons/flags/GB.png" alt="Country flag" />
                          </div>
                          <div className="ml-6">
                            <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Country:</p>
                            <h6 className="mb-0 text-sm leading-normal dark:text-white">Great Britain</h6>
                          </div>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Sales:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">1.400</h6>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Value:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">$190,700</h6>
                        </div>
                      </td>
                      <td className="p-2 text-sm leading-normal align-middle bg-transparent border-b whitespace-nowrap dark:border-white/40">
                        <div className="flex-1 text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Bounce:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">23.44%</h6>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td className="p-2 align-middle bg-transparent border-0 w-3/10 whitespace-nowrap">
                        <div className="flex items-center px-2 py-1">
                          <div>
                            <img src="./assets/img/icons/flags/BR.png" alt="Country flag" />
                          </div>
                          <div className="ml-6">
                            <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Country:</p>
                            <h6 className="mb-0 text-sm leading-normal dark:text-white">Brasil</h6>
                          </div>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-0 whitespace-nowrap">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Sales:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">562</h6>
                        </div>
                      </td>
                      <td className="p-2 align-middle bg-transparent border-0 whitespace-nowrap">
                        <div className="text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Value:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">$143,960</h6>
                        </div>
                      </td>
                      <td className="p-2 text-sm leading-normal align-middle bg-transparent border-0 whitespace-nowrap">
                        <div className="flex-1 text-center">
                          <p className="mb-0 text-xs font-semibold leading-tight dark:text-white dark:opacity-60">Bounce:</p>
                          <h6 className="mb-0 text-sm leading-normal dark:text-white">32.14%</h6>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div className="w-full max-w-full px-3 mt-0 lg:w-5/12 lg:flex-none">
            <div className="border-black/12.5 shadow-xl dark:bg-slate-850 dark:shadow-dark-xl relative flex min-w-0 flex-col break-words rounded-2xl border-0 border-solid bg-white bg-clip-border">
              <div className="p-4 pb-0 rounded-t-4">
                <h6 className="mb-0 dark:text-white">Categories</h6>
              </div>
              <div className="flex-auto p-4">
                <ul className="flex flex-col pl-0 mb-0 rounded-lg">
                  <li className="relative flex justify-between py-2 pr-4 mb-2 border-0 rounded-t-lg rounded-xl text-inherit">
                    <div className="flex items-center">
                      <div className="inline-block w-8 h-8 mr-4 text-center text-black bg-center shadow-sm fill-current stroke-none bg-gradient-to-tl from-zinc-800 to-zinc-700 dark:bg-gradient-to-tl dark:from-slate-750 dark:to-gray-850 rounded-xl">
                        <i className="text-white ni ni-mobile-button relative top-0.75 text-xxs"></i>
                      </div>
                      <div className="flex flex-col">
                        <h6 className="mb-1 text-sm leading-normal text-slate-700 dark:text-white">Devices</h6>
                        <span className="text-xs leading-tight dark:text-white/80">250 in stock, <span className="font-semibold">346+ sold</span></span>
                      </div>
                    </div>
                    <div className="flex">
                      <button className="group ease-in leading-pro text-xs rounded-3.5xl p-1.2 h-6.5 w-6.5 mx-0 my-auto inline-block cursor-pointer border-0 bg-transparent text-center align-middle font-bold text-slate-700 shadow-none transition-all dark:text-white"><i className="ni ease-bounce text-2xs group-hover:translate-x-1.25 ni-bold-right transition-all duration-200" aria-hidden="true"></i></button>
                    </div>
                  </li>
                  <li className="relative flex justify-between py-2 pr-4 mb-2 border-0 rounded-xl text-inherit">
                    <div className="flex items-center">
                      <div className="inline-block w-8 h-8 mr-4 text-center text-black bg-center shadow-sm fill-current stroke-none bg-gradient-to-tl from-zinc-800 to-zinc-700 dark:bg-gradient-to-tl dark:from-slate-750 dark:to-gray-850 rounded-xl">
                        <i className="text-white ni ni-tag relative top-0.75 text-xxs"></i>
                      </div>
                      <div className="flex flex-col">
                        <h6 className="mb-1 text-sm leading-normal text-slate-700 dark:text-white">Tickets</h6>
                        <span className="text-xs leading-tight dark:text-white/80">123 closed, <span className="font-semibold">15 open</span></span>
                      </div>
                    </div>
                    <div className="flex">
                      <button className="group ease-in leading-pro text-xs rounded-3.5xl p-1.2 h-6.5 w-6.5 mx-0 my-auto inline-block cursor-pointer border-0 bg-transparent text-center align-middle font-bold text-slate-700 shadow-none transition-all dark:text-white"><i className="ni ease-bounce text-2xs group-hover:translate-x-1.25 ni-bold-right transition-all duration-200" aria-hidden="true"></i></button>
                    </div>
                  </li>
                  <li className="relative flex justify-between py-2 pr-4 mb-2 border-0 rounded-b-lg rounded-xl text-inherit">
                    <div className="flex items-center">
                      <div className="inline-block w-8 h-8 mr-4 text-center text-black bg-center shadow-sm fill-current stroke-none bg-gradient-to-tl from-zinc-800 to-zinc-700 dark:bg-gradient-to-tl dark:from-slate-750 dark:to-gray-850 rounded-xl">
                        <i className="text-white ni ni-box-2 relative top-0.75 text-xxs"></i>
                      </div>
                      <div className="flex flex-col">
                        <h6 className="mb-1 text-sm leading-normal text-slate-700 dark:text-white">Error logs</h6>
                        <span className="text-xs leading-tight dark:text-white/80">1 is active, <span className="font-semibold">40 closed</span></span>
                      </div>
                    </div>
                    <div className="flex">
                      <button className="group ease-in leading-pro text-xs rounded-3.5xl p-1.2 h-6.5 w-6.5 mx-0 my-auto inline-block cursor-pointer border-0 bg-transparent text-center align-middle font-bold text-slate-700 shadow-none transition-all dark:text-white"><i className="ni ease-bounce text-2xs group-hover:translate-x-1.25 ni-bold-right transition-all duration-200" aria-hidden="true"></i></button>
                    </div>
                  </li>
                  <li className="relative flex justify-between py-2 pr-4 border-0 rounded-b-lg rounded-xl text-inherit">
                    <div className="flex items-center">
                      <div className="inline-block w-8 h-8 mr-4 text-center text-black bg-center shadow-sm fill-current stroke-none bg-gradient-to-tl from-zinc-800 to-zinc-700 dark:bg-gradient-to-tl dark:from-slate-750 dark:to-gray-850 rounded-xl">
                        <i className="text-white ni ni-satisfied relative top-0.75 text-xxs"></i>
                      </div>
                      <div className="flex flex-col">
                        <h6 className="mb-1 text-sm leading-normal text-slate-700 dark:text-white">Happy users</h6>
                        <span className="text-xs leading-tight dark:text-white/80"><span className="font-semibold">+ 430 </span></span>
                      </div>
                    </div>
                    <div className="flex">
                      <button className="group ease-in leading-pro text-xs rounded-3.5xl p-1.2 h-6.5 w-6.5 mx-0 my-auto inline-block cursor-pointer border-0 bg-transparent text-center align-middle font-bold text-slate-700 shadow-none transition-all dark:text-white"><i className="ni ease-bounce text-2xs group-hover:translate-x-1.25 ni-bold-right transition-all duration-200" aria-hidden="true"></i></button>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <footer className="pt-4">
          <div className="w-full px-6 mx-auto">
            <div className="flex flex-wrap items-center -mx-3 lg:justify-between">
              <div className="w-full max-w-full px-3 mt-0 mb-6 shrink-0 lg:mb-0 lg:w-1/2 lg:flex-none">
                <div className="text-sm leading-normal text-center text-slate-500 lg:text-left">
                  ©
                  <script>
                    document.write(new Date().getFullYear() + ",");
                  </script>
                  made with <i className="fa fa-heart"></i> by
                  <a href="https://www.creative-tim.com" className="font-semibold text-slate-700 dark:text-white" target="_blank">Creative Tim</a>
                  for a better web.
                </div>
              </div>
              <div className="w-full max-w-full px-3 mt-0 shrink-0 lg:w-1/2 lg:flex-none">
                <ul className="flex flex-wrap justify-center pl-0 mb-0 list-none lg:justify-end">
                  <li className="nav-item">
                    <a href="https://www.creative-tim.com" className="block px-4 pt-0 pb-1 text-sm font-normal transition-colors ease-in-out text-slate-500" target="_blank">Creative Tim</a>
                  </li>
                  <li className="nav-item">
                    <a href="https://www.creative-tim.com/presentation" className="block px-4 pt-0 pb-1 text-sm font-normal transition-colors ease-in-out text-slate-500" target="_blank">About Us</a>
                  </li>
                  <li className="nav-item">
                    <a href="https://creative-tim.com/blog" className="block px-4 pt-0 pb-1 text-sm font-normal transition-colors ease-in-out text-slate-500" target="_blank">Blog</a>
                  </li>
                  <li className="nav-item">
                    <a href="https://www.creative-tim.com/license" className="block px-4 pt-0 pb-1 pr-0 text-sm font-normal transition-colors ease-in-out text-slate-500" target="_blank">License</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </footer> */}
      </div>
    </DefaultLayout>
  );
}

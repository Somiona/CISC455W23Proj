import 'styles/globals.css'
import type { AppProps } from 'next/app'
import React from "react";
import { config } from '@fortawesome/fontawesome-svg-core'
import '@fortawesome/fontawesome-svg-core/styles.css'
import { Open_Sans } from 'next/font/google'

const open_sans = Open_Sans({
  subsets: ["latin"],
  weight: ["300", "400", "600", "700"],
  variable: '--font-open-sans',
})

config.autoAddCss = false

export default function App({ Component, pageProps }: AppProps) {
  return <React.StrictMode>
    <Component {...pageProps} />
  </React.StrictMode>
}

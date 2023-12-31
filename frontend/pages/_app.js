import "@styles/globals.css";
import { useEffect } from "react"
import Head from 'next/head'

// redux
import { Provider } from "react-redux";
import { store } from "@redux/store";
import { redirectHandler } from "@redux/modules/auth/thunks"

// toast
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    store.dispatch(redirectHandler())
  })
  
  return (
    <Provider store={store}>
      <Head>
        <meta name="description" content="Jiva" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Component {...pageProps} />
      <ToastContainer />
    </Provider>
  );
}

export default MyApp;

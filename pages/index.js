import Head from "next/head";
import Layout from "@components/Layout";

export default function Home() {
  return (
    <Layout navType="topbar">
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
    </Layout>
  );
}

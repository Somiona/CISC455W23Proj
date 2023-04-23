import { FC } from "react";

import { useRouter } from "next/router";
import { NextSeo } from "next-seo";

import { appConfig } from "utils/config";
import Head from "next/head";

type IMetaProps = {
  title?: string;
  description?: string;
  canonical?: string;
};

const Meta: FC = (props: IMetaProps) => {
  const router = useRouter();
  const title: string = props.title ?? appConfig.title;
  const desc = `${appConfig.description} - By ${appConfig.authors.toString()}`;
  const description: string = props.description ?? desc;
  const canonical: string = props.canonical ?? router.asPath;

  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width,initial-scale=1" key="viewport" />
        <meta charSet="UTF-8" key="charset" />
      </Head>
      <NextSeo
        title={title}
        description={description}
        canonical={canonical}
        openGraph={{
          title,
          description,
          url: canonical,
          locale: appConfig.locale,
          site_name: appConfig.site_name,
        }}
      />
    </>
  );
};

export default Meta;

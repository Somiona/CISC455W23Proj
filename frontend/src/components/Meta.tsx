// Author: Somiona Tian (17ht13@queensu.ca)
// Disclaimer: Styles based on Argon Dashboard 2
import { FC } from "react";

import { useRouter } from "next/router";
import { NextSeo } from "next-seo";

import { appConfig } from "utils/config";
import Head from "next/head";

type IconResolution = 16 | 32 | 48 | 64 | 128 | 256;

type IconLinkProps = {
  basePath: string;
  resolution: IconResolution;
};

const SiteIcon: FC<IconLinkProps> = (props: IconLinkProps) => {
  const res = `${props.resolution}x${props.resolution}`;

  return (
    <link
      rel="icon"
      type="image/png"
      sizes={res}
      href={`${props.basePath}/favicon-${res}.png`}
      key={`icon${props.resolution}`}
    />
  );
};

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
  const iconSizes: Array<IconResolution> = [16, 32, 64, 128, 256];

  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width,initial-scale=1" key="viewport" />
        <meta charSet="UTF-8" key="charset" />
        <link rel="apple-touch-icon" href={`${router.basePath}/apple-touch-icon.png`} key="apple" />
        {iconSizes.map((resolution: IconResolution) => (
          <SiteIcon basePath={router.basePath} resolution={resolution} key={`icon_${resolution}`} />
        ))}
        <link rel="icon" href={`${router.basePath}/favicon.ico`} key="favicon" />
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

var klaroConfig = {
    elementID: 'klaro',
    groupByPurpose: true,
    storageMethod: 'cookie',
    cookieName: 'klaro',
    cookieExpiresAfterDays: 365,
    privacyPolicy: '/#privacy',
    default: false,
    mustConsent: false,
    acceptAll: true,
    hideDeclineAll: false,
    hideLearnMore: false,
    translations: {
        de: {
            consentModal: {
                description:
                    'Hier können Sie einsehen und anpassen, welche Information wir über Sie sammeln. Einträge die als "Beispiel" gekennzeichnet sind dienen lediglich zu Demonstrationszwecken und werden nicht wirklich verwendet.',
            },
            cloudflare: {
                description: 'Schutz gegen DDoS-Angriffe',
            },
            konsens: {
                description:
                    'Anonyme Besucherstatistiken',
            },
            purposes: {
                analytics: 'Besucher-Statistiken',
                security: 'Sicherheit',
            },
        },
        en: {
            consentModal: {
                description:
                    'This website uses third-party applications. To protect and manage your privacy you can review and control these apps here.',
            },
            konsens: {
                description: 'Collecting of anonymous visitor statistics',
            },
            cloudflare: {
                description: 'Protection against DDoS attacks',
            },
            purposes: {
                analytics: 'Analytics',
                security: 'Security',
            },
        },
    },
    apps: [
        {
            name: 'konsens',
            default: true,
            title: 'Konsens',
            purposes: ['analytics'],
            cookies: [
                /^.*kip.*$/,
            ],
            required: false,
            optOut: false,
            onlyOnce: true,
        },
        {
            name: 'cloudflare',
            title: 'Cloudflare',
            purposes: ['security'],
            required: true,
        },
    ],
};

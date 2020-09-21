module.exports = {
    client: {
        service: {
            name: 'tech_toys',
            // URL to the GraphQL API
            url: 'http://localhost:8000/api/',
        },
        // Files processed by the extension
        includes: [
            'src/**/*.vue',
            'src/**/*.js',
        ],
    },
}
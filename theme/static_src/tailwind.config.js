/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 * Color palette generator: http://colormind.io/bootstrap/
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            screens: {
                'print': { 'raw': 'print' },
            }
        },
        fontFamily: {
            poppins: ['Poppins', 'sans-serif'],
            asap: ['Asap', 'sans-serif'],
        },
        colors: {
            transparent: 'transparent',
            main: {
                50: '#ecf3f9',
                100: '#c6dbec',
                200: '#9fc3df',
                300: '#79abd2',
                DEFAULT: '#5A98C8',
                400: '#5394c6',
                500: '#397aac',
                600: '#2d5f86',
                700: '#204460',
                800: '#132939',
                900: '#060e13',
            },
            shade: {
                light: {
                    DEFAULT: '#F0EEEC',
                    50: '#f4f2f1',
                    100: '#ddd9d4',
                    200: '#c7bfb8',
                    300: '#b0a69b',
                    400: '#9a8c7f',
                    500: '#807365',
                    600: '#64594f',
                    700: '#474038',
                    800: '#2b2622',
                    900: '#0e0d0b',
                },
                dark: {
                    50: '#edf1f8',
                    100: '#c8d6e9',
                    200: '#a3badb',
                    300: '#7f9fcd',
                    400: '#5a83be',
                    500: '#416aa5',
                    600: '#325280',
                    DEFAULT: '#31507D',
                    700: '#243b5c',
                    800: '#162337',
                    900: '#070c12',
                }
            },
            accent: {
                light: {
                    50: '#eaf9fa',
                    100: '#c1edf0',
                    200: '#98e1e6',
                    300: '#6fd5dc',
                    400: '#46c9d2',
                    DEFAULT: '#4ECBD4',
                    500: '#2dafb9',
                    600: '#238890',
                    700: '#196167',
                    800: '#0f3a3e',
                    900: '#051315',
                },
                dark: {
                    50: '#edf5f8',
                    100: '#c8e1e9',
                    200: '#a4cddb',
                    300: '#7fb9cd',
                    400: '#5aa5be',
                    DEFAULT: '#4B9DB8',
                    500: '#418ca5',
                    600: '#326d80',
                    700: '#244e5b',
                    800: '#162f37',
                    900: '#071012',
                }
            },
            white: '#fff',
            black: '#000',
            error: {
                light: '#f8d7da',
                DEFAULT: '#DC3545',
                dark: '#721c24',
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}

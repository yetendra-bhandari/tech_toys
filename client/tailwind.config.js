module.exports = {
  purge: [],
  theme: {
    extend: {
      spacing: {
        0.5: '0.125rem',
        1.5: '0.375rem',
        72: '18rem',
        80: '20rem',
        96: '24rem',
        128: '32rem'
      },
      fontSize: {
        '1.5xl': '1.4rem'
      },
      borderRadius: {
        'xl': '1rem'
      },
      maxWidth: {
        '2xs': '16rem',
        '3xs': '12rem',
        '4xs': '10rem',
        '1/2': '50%',
        '3/4': '75%',
      },
      maxHeight: {
        '4/5': '80%',
      },
      colors: {
        color1: 'var(--color1)',
        color2: 'var(--color2)',
        color3: 'var(--color3)',
        color4: 'var(--color4)',
        color5: 'var(--color5)',
        color6: 'var(--color6)',
        color7: 'var(--color7)',
        color8: 'var(--color8)',
        color9: 'var(--color9)'
      },
      fontFamily: {
        'title': 'Quicksand',
        'body': 'Livvic'
      },
      inset: {
        '-6': '-1.5rem'
      },
      minHeight: {
        60: '15rem',
      }
    },
  },
  variants: {
    backgroundColor: ['responsive', 'hover', 'focus', 'active'],
    borderColor: ['responsive', 'hover', 'focus', 'active', 'group-hover'],
    textColor: ['responsive', 'hover', 'focus', 'active', 'group-hover'],
  },
  plugins: []
}
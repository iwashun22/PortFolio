export default {
  data: {
    particles: {
      number: {
        value: 20,
        density: {
          enable: true,
          value_area: 1600
        }
      },
      shape: {
        type: 'circle',
        stroke: {
          width: 0,
          color: '#ffcc00'
        }
      },
      color: {
        value: '#AAD8D3'
      },
      opacity: {
        value: 1,
        random: false,
        anim: {
          enable: false,
          speed: 1,
          opacity_min: 0.1,
          sync: false
        }
      },
      size: {
        value: 50,
        random: false,
        anim: {
          enable: false,
          speed: 20,
          size_min: 40,
          sync: false
        }
      },
      line_linked: {
        enable: true,
        distance: 110,
        color: '#ffffff',
        opacity: 0,
        width: 1
      },
      move: {
        speed: 5,
        straight: false,
        direction: 'none',
        out_mode: 'out'
      }
    },
    interactivity: {
      detect_on: 'canvas',
      events: {
        onhover: {
          enable: true,
          mode: 'bubble'
        },
        onclick: {
          enable: true,
          mode: 'push'
        }
      },
      modes: {
        grab: {
          distance: 200,
          line_linked: {
            opacity: 1
          }
        },
        repulse: {
          distance: 200
        },
        bubble: {
          distance: 200,
          size: 72,
          opacity: 8,
          duration: 2,
          speed: 3
        },
        push: {
          particles_nb: 3
        },
        remove: {
          particles_nb: 2
        }
      }
    },
    retina_detect: true,
    resize: true
  }
}

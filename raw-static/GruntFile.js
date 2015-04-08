module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Package
    pkg: grunt.file.readJSON('package.json'),

    /**
     * Watch
     */
    watch: {
      sass: {
        files: 'materialize-src/sass/{,*/}*.{scss,sass}',
        tasks: ['sass:dist']
      }
    },

    sass: {
      dist: {
        options: {
          style: 'expanded', //'compressed',
          compass: true
        },
        files: {
          '../static/css/style.css': '../static/css/aboutrape.css'
        }
      }
    },

    // Uglify
    uglify: {
      options: {
        banner: '/*! <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'materialize-src/js/*.js',
        dest: '../static/js/test.min.js'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['uglify', 'sass', 'watch']);

};
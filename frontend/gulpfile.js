'use strict';

var gulp = require('gulp');
var rename = require("gulp-rename");
var util = require('gulp-util');
var clean = require('gulp-clean');

gulp.task('clean-theme', function () {
  
  gulp.src('src/compoments/custom/*.vue', {read: false})
    .pipe(clean());

  // gulp.src(['src/services/custom/*.js'])
  //   .pipe(clean());

  // gulp.src(['src/store/modules/custom/*.js'])
  //   .pipe(clean());

  // gulp.src(['src/variables.scss'])
  //   .pipe(clean());

});


gulp.task('theme', function () {


  // CUSTOM IMAGES
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/images/**/*'])
    .pipe(gulp.dest('static/images/'));

  // CONFIG FILE JS
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/settings/config.js'])
    .pipe(rename('config.js'))
    .pipe(gulp.dest('src/'));

  // CONFIG FILE JS
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/settings/' + (util.env.deploy ? util.env.deploy : 'staging') + '.js'])
    .pipe(rename('api.js'))
    .pipe(gulp.dest('src/'));

  // CUSTOM CSS
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/settings/variables.scss'])
    .pipe(rename('variables.scss'))
    .pipe(gulp.dest('src/'));

  // CUSTOM COMPONENTS
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/components/**/*'])
    .pipe(gulp.dest('src/components/custom'));

  // CUSTOM SERVICES
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/services/**/*'])
    .pipe(gulp.dest('src/services/custom'));
  
  // CUSTOM MODULES
  gulp.src(['./themes/' + (util.env.theme_name ? util.env.theme_name : 'default') + '/store/modules/**/*'])
    .pipe(gulp.dest('src/modules/custom'));

});

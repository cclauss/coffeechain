export default {
  title: 'Smart Label',
  GA_KEY: 'UA-115379270-1',

  default_language: 'en',
  available_langues: ['en'],
  
  custom_routes: [{
    path: '/promotion',
    name: 'promotion',
    component: () => import('@/components/custom/Promotion'),
    props: true
  }],
  
  custom_services: [],
  custom_modules: [],
}

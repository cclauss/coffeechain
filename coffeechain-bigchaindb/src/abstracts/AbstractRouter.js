import express from 'express';
import { NotFoundErrorHandler, HttpErrorHandler } from '../handlers/ErrorHandler';

export default class AbstractRouter {
  constructor () {
    if (this.constructor === AbstractRouter) {
      throw new Error('Cannot construct instances of abstract class AbstractRouter directly. Must extend it.');
    }
    if (this.registerRoutes === AbstractRouter.prototype.registerRoutes) {
      throw new Error('Must implement/override abstract method registerRoutes');
    }
    this.router = express.Router();
    this.router.use(express.urlencoded({
      extended: false
    }));
    this.router.use(express.json());
    this.registerRoutes();
    this.registerErrorHandlers();
  }

  registerRoutes () { // eslint-disable-line
    throw new Error('Do not call abstract method registerRoutes from child.');
  }

  registerErrorHandlers () {
    this.router.use(NotFoundErrorHandler);
    this.router.use(HttpErrorHandler);
  }

  getRouter () {
    return this.router;
  }
}

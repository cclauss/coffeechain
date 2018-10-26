import AbstractRouter from '../abstracts/AbstractRouter';
import CRABService from '../services/CRABService';
import ValidatorService from '../services/ValidatorService';

export default class AssetCRABRouter extends AbstractRouter {
  /**
   *
   * @param {string} assetName name of the asset
   */
  constructor (assetName) {
    super();
    this.crabService = new CRABService(assetName);
    this.validatorService = new ValidatorService(assetName);
  }

  /**
   * Overriden from AbstractRouter
   * Required by AbstractRouter to initialize and register routes
   */
  registerRoutes () {
    this.router.post('/', async (req, res) => {
      const { keypair, metadata } = req.body;
      const isValidSchema = await this.validatorService.validate(metadata);
      if (isValidSchema) {
        this.crabService.createAsset(keypair, metadata).then((value) => {
          res.json(value);
        });
      } else {
        res.json({ error: 'Asset Schema Validation Failed' });
      }
    });

    this.router.get('/:assetid', (req, res) => {
      const { assetid } = req.params;
      this.crabService.retrieveAsset(assetid).then((value) => {
        res.json(value);
      });
    });

    this.router.get('/', (req, res) => {
      this.crabService.retrieveAllAssets().then((value) => {
        res.json(value);
      });
    });

    this.router.get('/history/:assetid', (req, res) => {
      const { assetid } = req.params;
      this.crabService.assetHistory(assetid).then((value) => {
        res.json(value);
      });
    });

    this.router.put('/:assetid', async (req, res) => {
      const {
        keypair, metadata, topublickey, assetid
      } = req.body;
      const isValidSchema = await this.validatorService.validate(metadata);
      if (isValidSchema) {
        this.crabService.appendAsset(assetid, keypair, topublickey, metadata).then((value) => {
          res.json(value);
        });
      } else {
        res.json({ error: 'Asset Schema Validation Failed' });
      }
    });

    this.router.delete('/:assetid', (req, res) => {
      const { keypair } = req.body;
      const { assetid } = req.params;
      this.crabService.burnAsset(assetid, keypair).then((value) => {
        res.json(value);
      });
    });
  }
}

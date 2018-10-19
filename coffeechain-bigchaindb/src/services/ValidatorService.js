import CRABService from './CRABService';
import ORMService from './ORMService';

export default class ValidatorService {

  constructor(assetName) {
    this.assetName = assetName;
    this.schema = new ORMService().getModel(this.assetName)._schema;
  }

  async validate(data, schema = this.schema) {
    let isValid = true;
    for (const key of Object.keys(data)) {
      if (typeof (schema[key]) === 'object' && ('type' in schema[key])) {
        isValid = await this.validBDBObject(data[key], schema[key]);
        if (!isValid) break;
      } else if (typeof (schema[key]) === 'object') {
        isValid = await this.validate(data[key], schema[key]);
        if (!isValid) break;
      } else if (typeof (data[key]) !== schema[key]) {
        isValid = false;
        break;
      }

    }
    return isValid;
  };

  async validBDBObject(data, schema) {
    let isValid = true;
    if (schema.type === 'single') {
      const status = await this.assetExists(schema.asset, data).then(status => {
        return status;
      });
      if (!status) {
        isValid = false;
      }
    } else {
      for (const assetid of data) {
        const status = await this.assetExists(schema.asset, assetid).then(status => {
          return status;
        });
        if (!status) {
          isValid = false;
          break;
        }
      }
    }
    return isValid;
  }


  assetExists(assetName, assetid) {
    const service = new CRABService(assetName);
    return service.retrieveAsset(assetid).then(asset => {
      return (asset.length > 0);
    });
  };
}

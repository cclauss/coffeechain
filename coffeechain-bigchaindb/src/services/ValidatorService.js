import CRABService from './CRABService';
import ORMService from './ORMService';

export default class ValidatorService {

  constructor(assetName){
    this.assetName = assetName;
  }

  async validate(data){
    const schema = new ORMService().getModel(this.assetName)._schema;
    let isValid = true;
    for (const key of Object.keys(schema)) {
      if (typeof (schema[key]) === 'object') {
        const assetname = schema[key].asset;
        if (schema[key].type === 'single') {
          console.log("here");
          const assetid = data[key];
          const status = await this.assetExists(assetname, assetid).then(status => {
            console.log(assetname," " ,assetid, " ",status);
            return status;
          });
          if (!status) {
            isValid = false;
          }
        } else {
          for (const assetid of data[key]) {
            const status = await this.assetExists(assetname, assetid).then(status => {
              console.log(assetname," " ,assetid, " ",status);
              return status;
            });
            if (!status) {
              isValid = false;
              break;
            }
          }
        }
        if (!isValid) break;
      } else if (typeof (data[key]) !== schema[key]) {
        isValid = false;
        break;
      }
  
    }
    return isValid;
  };
  
  
  assetExists(assetName, assetid){
    const service = new CRABService(assetName);
    return service.retrieveAsset(assetid).then(asset => {
      return (asset.length > 0);
    });
  };
}

import ORMService from './ORMService';

export default class CRABService {
  /**
   * @param {string} assetName name of the asset
   */
  constructor (assetName) {
    this.assetModel = new ORMService().getModel(assetName);
  }

  /**
   * Create the Asset on BigchainDB
   *
   * @param {Object} userKeypair Ed25519 keypair
   * @param {Object} metadata Metadata that will be used during asset creation
   */
  createAsset (userKeypair, metadata) {
    let id;
    if (Object.prototype.hasOwnProperty.call(metadata, 'key')) {
      id = metadata.key;
      // delete metadata.key;         // un-comment if you want to remove duplicate key
    }
    return this.assetModel.create({
      keypair: userKeypair,
      data: metadata
    }, id).then((asset) => asset).catch((error) => Promise.resolve({
      error
    }));
  }

  /**
   * Retrieve the Asset using asset id
   *
   * @param {string} assetid asset id of the asset created on blockchain
   */
  retrieveAsset (assetid) {
    return this.assetModel
      .retrieve(assetid)
      .then((asset) => asset).catch((error) => Promise.resolve({
        error
      }));
  }

  /**
   *
   * Retrieve all the assets(of this asset type)
   */
  retrieveAllAssets () {
    return this.assetModel
      .retrieve()
      .then((asset) => asset).catch((error) => Promise.resolve({
        error
      }));
  }

  /**
   *
   * Append/Update/Spend the asset
   *
   * @param {string} assetid asset id of the asset created on blockchain
   * @param {Object} userKeypair Ed25519 keypair
   * @param {string} toPublicKey publicKey
   * @param {Object} metadata Asset Metadata
   */
  appendAsset (assetid, userKeypair, toPublicKey, metadata) {
    return this.assetModel
      .retrieve(assetid)
      .then((asset) => {
        if (asset.length) {
          return asset[0].append({
            toPublicKey,
            keypair: userKeypair,
            data: metadata
          });
        }
        throw new Error('Asset Not Found');
      }).catch((error) => Promise.resolve({
        error
      }));
  }

  /**
   *
   * Burn/Mark the asset unspendable
   *
   * @param {string} assetid asset id of the asset created on blockchain
   * @param {Object} userKeypair Ed25519 keypair
   */
  burnAsset (assetid, userKeypair) {
    return this.assetModel
      .retrieve(assetid)
      .then((asset) => {
        if (asset.length) {
          return asset[0].burn({
            keypair: userKeypair
          });
        }
        throw Error('Asset Not Found');
      }).catch((error) => Promise.resolve({
        error
      }));
  }

  assetHistory (assetid) {
    return this.assetModel
      .retrieve(assetid)
      .then((asset) => asset[0].transactionHistory).catch((error) => Promise.resolve({
        error
      }));
  }
}

class ToDo {
    _id: string;
    estimated_time: number;
    title: string; 
    creation_time: string;

    constructor(_id:string, estimated_time= 0, title:string, creation_time:string){
        this._id = _id;
        this.estimated_time = estimated_time;
        this.title = title;
        this.creation_time = creation_time;

    }

}
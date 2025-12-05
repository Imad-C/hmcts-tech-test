export interface TodoPayload {
  title: string;
  description?: string;
  status: string;
  due: Date;
}

export interface Todo {
  id: number;
  title: string;
  description?: string;
  status: string;
  due: Date;
}
